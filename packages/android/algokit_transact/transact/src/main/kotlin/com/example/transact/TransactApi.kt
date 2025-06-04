package com.example.transact

import uniffi.algokit_transact_ffi.*

class TransactApi {
    companion object {
        init {
            try {
                System.loadLibrary("algokit_transact_ffi")
            } catch (e: UnsatisfiedLinkError) {
                throw RuntimeException("Failed to load native library: ${e.message}", e)
            }
        }
    }

    fun createAddressFromPubKey(pubKey: ByteArray): Address {
        return addressFromPubKey(pubKey)
    }

    fun createAddressFromString(address: String): Address {
        return addressFromString(address)
    }

    fun encodeTransaction(transaction: Transaction): ByteArray {
        return encodeTransaction(transaction)
    }

    fun decodeTransaction(bytes: ByteArray): Transaction {
        return decodeTransaction(bytes)
    }
}
